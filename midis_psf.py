#!/usr/bin/env  python

import os
import argparse
from astropy.io import fits
from astropy.wcs import WCS

ROOT = os.path.dirname(__file__)
PSF_MAP = os.path.join(ROOT, './data-{}/midis_psf_map.fits')
PSF_TMPL = os.path.join(ROOT, './data-{}/{}mas/HUDF_F560W_i2d-psf_inserted-original{}-cutout-bg-norm.fits')
LATEST_VERSION='v5'

def get_psf(ra_deg, dec_deg, psf_idx=None, filename_only=True, version=LATEST_VERSION, pixscale=60):
    """Get MIDI PSF model for (ra,dec).

    Parameters
    ----------
    ra_deg: float
       ra in degrees
    deg_deg: float
       deg in degrees
    filename_only: bool (default: True)
       return filename only
    version: string (default: latest)
       version of psf to use
    pixscale: int (default: 60)
       pixscale in mas (30, 40 or 60)

    Returns
    -------
    numpy.ndarray with psf, or the filename if filename_only==True

    """

    if psf_idx is None:
        with fits.open(PSF_MAP.format(version)) as hdu:
            map_wcs = WCS(hdu[0].header)
            map_data = hdu[0].data

            x, y = map_wcs.all_world2pix(ra_deg, dec_deg, 0)

            try:
                # nearest pixel
                psf_idx = int(map_data[int(y), int(x)])
            except:
                psf_idx = 0

    filename = os.path.abspath(PSF_TMPL.format(version, pixscale, psf_idx))

    if psf_idx == 0:
        print(f"No psf for ({ra_deg}, {dec_deg}).")
        return 0
    elif filename_only:
        print(filename)
        return filename
    else:
        with fits.open(filename) as hdu2:
            return hdu2[0].data


def main(args=None):
    parser = argparse.ArgumentParser(description="""Get MIDI PSF model for (ra,dec).""")

    parser.add_argument("ra_deg", type=float,
                        help="ra in degrees")
    parser.add_argument("dec_deg", type=float,
                        help="dec in degrees")
    parser.add_argument('-i', '--psf_idx', type=int, default=None,
                        help="psf index (supersedes coordinates)")
    parser.add_argument('-f', '--filename_only', type=bool, default=True,
                        help="return filename only (default: true)")
    parser.add_argument('-v', '--version', type=str, default=LATEST_VERSION,
                        help="version of psf to use (default: latest)")
    parser.add_argument('-p', '--pixscale', type=int, default=60,
                        choices=[30, 40, 60], help="pixscale in mas")

    args = parser.parse_args(args)

    return get_psf(args.ra_deg, args.dec_deg, args.psf_idx, args.filename_only, args.version, args.pixscale)


if __name__ == '__main__':
    main()
